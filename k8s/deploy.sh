#!/usr/bin/env bash

set -e

image_tag=$1
k8s_root_dir="url-shortener"
helm_release="url-shortener"

if [[ -z "${image_tag}" ]]; then
  echo "No image tag was provided. Usage:"
  echo "./deploy-k8s.sh \${image_tag}"
  exit 1
fi

helm upgrade ${helm_release} \
  --debug \
  --atomic \
  --install \
  --values ${k8s_root_dir}/values.yaml \
  --set image.tag="${image_tag}" \
  ${k8s_root_dir}