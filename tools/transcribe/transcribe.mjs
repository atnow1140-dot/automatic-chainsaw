// 使い方: node transcribe.mjs <音声or動画ファイル> [-o 出力.txt]
// モデルは npm パッケージ sts-whisper-small から読む（Hugging Face へは接続しない）
import { pipeline, env } from '@huggingface/transformers';
import { execFileSync } from 'child_process';
import { createRequire } from 'module';
import fs from 'fs';
import path from 'path';

const args = process.argv.slice(2);
const oIdx = args.indexOf('-o');
const outPath = oIdx >= 0 ? args[oIdx + 1] : null;
const input = args.find((a, i) => oIdx < 0 || (i !== oIdx && i !== oIdx + 1));
if (!input) {
  console.error('使い方: node transcribe.mjs <音声or動画ファイル> [-o 出力.txt]');
  process.exit(1);
}

// ffmpeg で 16kHz モノラルの float32 PCM に変換
const pcm = execFileSync('ffmpeg', ['-loglevel', 'error', '-i', input, '-ac', '1', '-ar', '16000', '-f', 'f32le', '-'], { maxBuffer: 1 << 30 });
const audio = new Float32Array(pcm.buffer, pcm.byteOffset, pcm.length / 4);

const require = createRequire(import.meta.url);
env.allowRemoteModels = false;
env.localModelPath = path.join(path.dirname(require.resolve('sts-whisper-small/package.json')), 'models') + '/';

const asr = await pipeline('automatic-speech-recognition', 'Xenova/whisper-small', { dtype: 'q8' });
const result = await asr(audio, { language: 'japanese', task: 'transcribe', chunk_length_s: 30, stride_length_s: 5, return_timestamps: true });

const lines = result.chunks.map(c => `[${c.timestamp[0]?.toFixed(1)}-${c.timestamp[1]?.toFixed(1)}] ${c.text.trim()}`);
const text = lines.join('\n') + '\n';
process.stdout.write(text);
if (outPath) fs.writeFileSync(outPath, text);
