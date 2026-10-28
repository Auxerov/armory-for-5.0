# armory (Blender 5.0+ Compatible)

[Download](https://github.com/Auxerov/armory-for-5.0/releases) &bullet; [Release Notes](https://github.com/Auxerov/armory-for-5.0/releases) &bullet; [Manual](https://github.com/armory3d/armory/wiki) &bullet; [Forums](https://forums.armory3d.org/)

Armory is an open-source 3D game engine focused on portability, minimal footprint and performance. The renderer is fully scriptable with deferred and forward paths supported out of the box.

Armory as a Blender add-on provides a full Blender integration, turning it into a complete game development tool and a unified workflow from start to finish.

![](http://armory3d.org/git/img1.jpg)

## Blender 5.0+ Compatibility & Fixes

This fork is patched and optimized specifically for **Blender 5.0+**:
- **`bgl` compatibility shim**: Built-in OpenGL compatibility shim for Blender 4.0+ and 5.0+ where `bgl` was removed.
- **Cycles Shader Nodes**: Updated shader converters and texture parsers for nodes deprecated or removed in Blender 5.0 (Combine/Separate HSV/RGB, PointDensity).
- **Modern Blender API Fixes**: Fixed `blf.size()` signature for Blender 4.1+/5.0+, empty PropertyGroup syntax, and Cycles tile size configuration.
- **Addon Loader & Auto-detection**: Includes root `__init__.py` and intelligent SDK path detection so it runs self-contained out of the box.

---

## Kurulum / How to Install in Blender 5.0

### Yöntem 1: Hazır Eklenti Paketi ile Kurulum (Önerilen / Recommended)

> [!IMPORTANT]
> GitHub'ın standart yeşil `Code -> Download ZIP` butonu, klasör adını `armory-for-5.0-main` olarak adlandırdığı için Python sözdizimi kuralı gereği (tire `-` ve nokta `.` karakterleri nedeniyle) Blender `ModuleNotFoundError: No module named 'armory-for-5'` hatası verir. Ayrıca GitHub kaynak kod zip'leri `Kha` derleyicisini (git submodule) içermez.
> Bu nedenle **her zaman Releases sayfasındaki hazır `armory.zip` paketini kullanın**.

1. **İndirin:** [Releases](https://github.com/Auxerov/armory-for-5.0/releases) sayfasına gidin ve en güncel sürümün altındaki **`armory.zip`** dosyasını indirin.
2. **Blender 5.0'da Kurun:**
   - Blender 5.0'ı açın.
   - **Edit** -> **Preferences** -> **Add-ons** sekmesine gidin.
   - Sağ üst köşedeki menüden (aşağı ok / dişli simgesi) **Install from Disk...** seçeneğine tıklayın.
   - İndirdiğiniz **`armory.zip`** dosyasını seçip **Install Add-on** deyin.
3. **Etkinleştirin:**
   - Arama kutusuna **Armory** yazın ve eklentinin yanındaki kutucuğu işaretleyin.
   - Eklenti, SDK yolunu otomatik algılayıp motoru hemen başlatacaktır (Harici Git veya Haxe kurulumu gerektirmez).

---

### Yöntem 2: Git ile Kurulum (Geliştiriciler İçin / For Developers)

Repoyu alt modülleriyle birlikte doğrudan klonlayıp kullanmak isterseniz:

```bash
# Alt modüllerle birlikte 'armory' adında bir klasöre klonlayın:
git clone --recursive https://github.com/Auxerov/armory-for-5.0.git armory
```

Ardından `armory` klasörünü Blender eklenti dizininize taşıyın veya Blender içinden `armory/armory.py` dosyasını kurun.


