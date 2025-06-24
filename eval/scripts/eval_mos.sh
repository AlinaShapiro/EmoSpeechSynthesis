#!/bin/bash

DATA_DIR="/home/alina/outputs/fastpitch/2_spkrds_eval"

declare -A emotion_scores
declare -A emotion_counts

start_time=$(date +%s)

while read -r filepath; do
    filename=$(basename "$filepath")

    if [[ "$filename" =~ (amused|anger|sleepiness|neutral) ]]; then
        emotion="${BASH_REMATCH[1]}"
        emotion_cap="$(tr '[:lower:]' '[:upper:]' <<< ${emotion:0:1})${emotion:1}"
    else
        echo "Emotion is not in the target set: $filename"
        continue
    fi

    mos=$(utmos "$filepath" 2>/dev/null | grep -oE '[0-9]+\.[0-9]+')

    if [[ -n "$mos" ]]; then
        echo $(echo "$mos" | bc)
    else
        echo "MOS is empty!"
        continue
    fi

    echo "$filename ($emotion_cap): MOS = $new_mos"

    current_sum="${emotion_scores[$emotion_cap]:-0}"
    current_count="${emotion_counts[$emotion_cap]:-0}"
    emotion_scores["$emotion_cap"]=$(echo "$current_sum + $new_mos" | bc)
    emotion_counts["$emotion_cap"]=$((current_count + 1))

done < <(find "$DATA_DIR" -type f -name "*.wav")

echo -e "\n=== Average MOS By Emotion ==="
for emotion in "${!emotion_scores[@]}"; do
    total="${emotion_scores[$emotion]}"
    count="${emotion_counts[$emotion]}"
    avg=$(echo "scale=2; $total / $count" | bc)
    echo "$emotion: $avg (n = $count)"
done

end_time=$(date +%s)
elapsed=$((end_time - start_time))
echo "Time of script inference: $elapsed sec"