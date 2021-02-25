import os
import sys
import xmltodict

def listPermissions(filename,manifests):
	file = sys.argv[1] + "/" + filename
	name = file.split("_",1)[1].split(".xml")[0]
	manifests[name] = []
	with open(file) as fd:
		doc = xmltodict.parse(fd.read())
	# List permissions
	for permissions in doc["manifest"]["uses-permission"]:
		try:
			manifests[name].append(permissions['@android:name'].split("permission.")[1])
		except IndexError:
			manifests[name].append(permissions['@android:name'].split("vending.")[1])

def separatePermissions(manifests,uniq,commom):
	for key in manifests: # each manifest
		uniq[key] = []
		for perm1 in manifests[key]: # each permission
			only = 1	
			for name in manifests: # each manifest
				if key == name:
					continue 
				for perm2 in manifests[name]: # each permission
					if perm1 == perm2:
						only = 0 # commom 
						if perm1 not in commom:
							commom.append(perm1)
			if only: # not commom
				if perm1 not in uniq[key]:
					uniq[key].append(perm1)		

if __name__ == '__main__':
	manifests = {}
	uniq = {}
	commom = []

	for filename in os.listdir(sys.argv[1]):
		if filename.endswith(".xml"):
			listPermissions(filename,manifests)
	
	print("\n############ Permissões por APK ############\n")
	for key in manifests:
		print(key,":",manifests[key],"\n")

	separatePermissions(manifests,uniq,commom)

	print("############ Permissões únicas das APKS ############\n")
	for key in uniq:
		print(key,":",uniq[key],"\n")

	print("############ Permissões comuns das APKS ############\n")
	print(commom)