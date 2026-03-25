#!/bin/bash
echo "🧪 CS2 Educational Sim - Otomatik Kurulum!"
echo "ZIP çıkartılıyor..."

# ZIP otomatik çıkart
if [ -f "cs2_educational_sim.zip" ]; then
    unzip -o cs2_educational_sim.zip
    echo "✅ ZIP çıkartıldı!"
fi

# Bağımlılıklar
pip install pymem pygame numpy

echo "🎉 HAZIR! CS2 bot match aç → python main.py"
echo "📁 Dosyalar: $(ls -la)"
