import os

def run_segregation_backup(device, local_root):
    remote_root = "/sdcard/"
    # Common folders that contain 99% of user data
    folders_to_sweep = ["DCIM", "Pictures", "Download", "Documents", "Movies", "Music", "Android/media"]
    
    for folder in folders_to_sweep:
        remote_folder = os.path.join(remote_root, folder).replace("\\", "/")
        print(f"> Accessing: {remote_folder}")
        
        # Use 'ls -R' to get every file inside the folder recursively
        files_listing = device.shell(f"find '{remote_folder}' -type f")
        
        if "Permission denied" in files_listing or not files_listing.strip():
            print(f"  Access Denied or Empty: {folder}")
            continue

        files = files_listing.split('\n')
        
        for remote_path in files:
            remote_path = remote_path.strip()
            if not remote_path: continue
            
            # Create the matching local path
            # This turns /sdcard/DCIM/Photo.jpg into C:/Backup/DCIM/Photo.jpg
            relative_path = remote_path.replace(remote_root, "")
            local_path = os.path.join(local_root, relative_path)
            
            # Ensure the local folder exists
            os.makedirs(os.path.dirname(local_path), exist_ok=True)
            
            if not os.path.exists(local_path):
                try:
                    print(f"  Copying: {os.path.basename(remote_path)}")
                    device.pull(remote_path, local_path)
                except:
                    print(f"  Could not pull: {remote_path}")