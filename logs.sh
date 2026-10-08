#!/bin/bash

# Créer un fichier de log
LOG="api_test_$(date +%Y%m%d_%H%M%S).log"

# Tester chaque endpoint
echo "Tests API - $(date)" >> $LOG
curl http://localhost:8000/books >> $LOG
echo "\n" >> $LOG

echo "Test terminé. Résultats dans $LOG"