#!/usr/bin/env bash
# Auto-activate Python venv
if [ -d "venv/Scripts" ]; then
    source venv/Scripts/activate
    echo "✅ Virtual environment activated!"
else
    echo "⚠️ venv not found. Create one with: python -m venv venv"
fi