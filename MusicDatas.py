import json
import sys
import UnityPy
import zipfile

UnityPy.set_assetbundle_decrypt_key(b"Big_True'sOrzmic")
with zipfile.ZipFile(sys.argv[1]) as apk:
    with apk.open("assets/basegamedatas") as f:
        env = UnityPy.load(f)
for obj in env.objects:
    data = obj.read()
    if data.name == "MusicDatas":
        data = data.script
        break
songs = json.loads(bytes(data))["musicDatas"]
print(songs)
with open("notes.csv", "w") as notes:
    for song in songs:
        counts = []
        for level in song["Difficulties"]:
            counts.append(str(level["NoteCount"]))
        notes.write(",".join(counts))
        notes.write("\n")