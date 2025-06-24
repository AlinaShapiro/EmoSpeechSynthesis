import os
import json
import numpy as np
from collections import defaultdict
from glob import glob


PRED_DIR = "/home/alina/repos/EmoSpeechSynthesis/eval/Emotion2Vec/outputs/FastPitch_ft_st_4000_lr_2e_4_batch_32_4_spkr"

valid_emotions = {"anger", "amused", "sleepiness", "neutral"}

counts = defaultdict(int)
correct = defaultdict(int)

for json_path in glob(f"{PRED_DIR}/*.json"):
    fname = os.path.basename(json_path)
    gt_emotion = fname.split("_")[0]
    
    if gt_emotion not in valid_emotions:
        continue

    with open(json_path) as f:
        data = json.load(f)
    labels = data[0]["labels"]
    scores = data[0]["scores"]

    pred_idx = int(np.argmax(scores))
    pred_emotion = labels[pred_idx].split("/")[-1] 
    print(f"{pred_emotion=}   ==== {gt_emotion=}")

    counts[gt_emotion] += 1
    if pred_emotion == "angry" and gt_emotion == "anger":
        correct[gt_emotion] += 1
    elif pred_emotion == "sad" and gt_emotion == "sleepiness":
        correct[gt_emotion] += 1
    elif pred_emotion == "happy" and gt_emotion == "amused":
        correct[gt_emotion] += 1
    elif pred_emotion == gt_emotion:
        correct[gt_emotion] += 1

recalls = {}
for emo in valid_emotions:
    if counts[emo] == 0:
        recalls[emo] = None
        continue
    recalls[emo] = correct[emo] / counts[emo]

print("Recall by emotion:")
for emo, r in recalls.items():
    if r is not None:
        print(f"  {emo}: {r:.4f}")

valid_recalls = [r for r in recalls.values() if r is not None]
recall_rate = sum(valid_recalls) / len(valid_recalls)
print(f"\nFinal Recall Rate: {recall_rate:.4f}")
