import os, zipfile, subprocess, sys

print("🧪 Otomatik Kurulum Başlıyor...")

# ZIP çıkart
if os.path.exists("cs2_educational_sim.zip"):
    with zipfile.ZipFile("cs2_educational_sim.zip", 'r') as zip_ref:
        zip_ref.extractall()
    os.remove("cs2_educational_sim.zip")
    print("✅ ZIP çıkartıldı!")

# Bağımlılıklar
subprocess.check_call([sys.executable, "-m", "pip", "install", "pymem", "pygame", "numpy"])

print("🎉 HAZIR! CS2 bot match aç → python main.py")
print("📁 Repo yapısı:")
os.system("tree ." if os.name == 'nt' else "ls -la")
