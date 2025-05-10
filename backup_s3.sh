#!/bin/bash
DIR=$1
BUCKET=$2
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
ARCHIVO="backup_${TIMESTAMP}.tar.gz"
LOG="/tmp/backup_${TIMESTAMP}.log"
echo "Iniciando backup: $(date)" > $LOG
tar -czf "/tmp/$ARCHIVO" $DIR
aws s3 cp "/tmp/$ARCHIVO" "s3://$BUCKET/$ARCHIVO"
echo "Backup completado: s3://$BUCKET/$ARCHIVO" | tee -a $LOG
rm "/tmp/$ARCHIVO"
