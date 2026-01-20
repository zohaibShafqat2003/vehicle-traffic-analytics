"""Setup script to organize raw videos into site-specific folders."""
import os
import shutil
from pathlib import Path
import re

def organize_raw_videos(data_dir: str = "data") -> None:
    """
    Organize raw videos from flat structure into site-wise folders.
    
    Naming convention: site{NN}_YYYYMMDD_HHMM_{condition}.mp4
    Example: site01_20260118_1800_day.mp4
    
    Creates:
        data/raw_videos/site01/
        data/raw_videos/site02/
        etc.
    """
    raw_videos_dir = os.path.join(data_dir, "raw_videos")
    
    if not os.path.exists(raw_videos_dir):
        print(f"❌ {raw_videos_dir} not found")
        return
    
    # Pattern: site{digits}_...
    pattern = re.compile(r"^(site\d+)_")
    
    files = [f for f in os.listdir(raw_videos_dir) 
             if os.path.isfile(os.path.join(raw_videos_dir, f))]
    
    organized = 0
    skipped = 0
    
    for filename in files:
        match = pattern.match(filename)
        if match:
            site_id = match.group(1)  # e.g., "site01"
            site_dir = os.path.join(raw_videos_dir, site_id)
            
            # Create site folder if it doesn't exist
            os.makedirs(site_dir, exist_ok=True)
            
            # Move file to site folder
            src = os.path.join(raw_videos_dir, filename)
            dst = os.path.join(site_dir, filename)
            
            if not os.path.exists(dst):
                shutil.move(src, dst)
                print(f"✅ {filename} → {site_id}/")
                organized += 1
            else:
                print(f"⚠️  {filename} already exists in {site_id}/")
        else:
            print(f"⏭️  Skipping '{filename}' (doesn't match naming convention)")
            skipped += 1
    
    print(f"\n📊 Summary: {organized} organized, {skipped} skipped")

if __name__ == "__main__":
    organize_raw_videos()
