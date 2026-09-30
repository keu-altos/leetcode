#!/bin/bash
cd /home/keu/PycharmProjects/leetcode

# --- Step 1: Rename category (top-level) folders ---
declare -A CATEGORIES=(
    ["1-D Dynamic Programming"]="d1_dynamic_programming"
    ["2-D Dynamic Programming"]="d2_dynamic_programming"
    ["Advanced Graphs"]="advanced_graphs"
    ["Arrays & Hashing"]="arrays_hashing"
    ["Backtracking"]="backtracking"
    ["Binary Search"]="binary_search"
    ["Bit Manipulation"]="bit_manipulation"
    ["Graphs"]="graphs"
    ["Greedy"]="greedy"
    ["Heap - Priority Queue"]="heap_priority_queue"
    ["Intervals"]="intervals"
    ["Linked List"]="linked_list"
    ["Math & Geometry"]="math_geometry"
    ["Sliding Window"]="sliding_window"
    ["Stack"]="stack"
    ["Trees"]="trees"
    ["Tries"]="tries"
    ["Two Pointers"]="two_pointers"
)

for root in src tests; do
    for old in "${!CATEGORIES[@]}"; do
        new="${CATEGORIES[$old]}"
        if [ -d "$root/$old" ]; then
            mv "$root/$old" "$root/$new"
        fi
    done
done

# --- Step 2: Rename problem folders (add "problem_" prefix, hyphens → underscores) ---
for root in src tests; do
    find "$root" -mindepth 2 -maxdepth 2 -type d | while read dir; do
        name="$(basename "$dir")"
        # Skip if already renamed (idempotent check)
        [[ "$name" == problem_* ]] && continue
        # "0001-two-sum" → "problem_0001_two_sum"
        new="problem_$(echo "$name" | tr '-' '_')"
        mv "$dir" "$(dirname "$dir")/$new"
    done
done

# --- Step 3: Add __init__.py so Python treats folders as packages ---
find src tests -type d | while read dir; do
    touch "$dir/__init__.py"
done

echo "=== Done. Resulting structure (src) ==="
find src -type d | sort
