#!/bin/bash

memory=(100 50 30 20 10)

processes=(50 30 20 10 5)

function first_fit() {
  for i in "${!memory[@]}"; do
    if [[ ${memory[$i]} -ge ${processes[$1]} ]]; then
      echo "Process ${processes[$1]} allocated to memory block ${memory[$i]}"
      memory[$i]=$((${memory[$i]} - ${processes[$1]}))
      return 0
    fi
  done

  echo "Process ${processes[$1]} could not be allocated"
  return 1
}

function worst_fit() {
  max_index=-1
  max_size=0

  for i in "${!memory[@]}"; do
    if [[ ${memory[$i]} -ge ${processes[$1]} && ${memory[$i]} -gt $max_size ]]; then
      max_index=$i
      max_size=${memory[$i]}
    fi
  done

  if [[ $max_index -eq -1 ]]; then
    echo "Process ${processes[$1]} could not be allocated"
    return 1
  fi

  echo "Process ${processes[$1]} allocated to memory block ${memory[$max_index]}"
  memory[$max_index]=$((${memory[$max_index]} - ${processes[$1]}))
  return 0
}

echo
echo "Allocation as per first fit"

for i in "${!processes[@]}"; do
  first_fit $i
done

memory=(100 50 30 20 10)

echo
echo "Allocation as per worst fit"

for i in "${!processes[@]}"; do
  worst_fit $i
done