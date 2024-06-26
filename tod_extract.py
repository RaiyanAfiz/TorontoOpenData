import requests
import os
import json


datasets = {"ttc-bus-delay-data", "ttc-subway-delay-data", "ttc-streetcar-delay-data"}

for target_dataset in datasets:

    #Make directory
    if not os.path.exists(target_dataset):
        os.mkdir(target_dataset)

    #Get CKAN Dataset
    base_url = "https://ckan0.cf.opendata.inter.prod-toronto.ca"
    url = base_url + "/api/3/action/package_show"
    payload = { "id": target_dataset}
    package = requests.get(url, params = payload).json()
    assert package['success'] is True

    #Write Package Data
    file_path = os.path.join(target_dataset, "package_info.json")
    f = open(file_path, "w")
    f.write(json.dumps(package))
    f.close()

    for idx, resource in enumerate(package["result"]["resources"]):

        if not resource["datastore_active"]:
            url = base_url + "/api/3/action/resource_show?id=" + resource["id"]
            resource_metadata = requests.get(url).json()
            assert resource_metadata['success'] is True

            
            file_name = resource_metadata['result']['name'].strip() + ".xlsx"
            file_path = os.path.join(target_dataset, file_name)
            url = resource_metadata['result']['url']
            
            #Write Data to Excel Files
            f = open(file_path, "wb")
            response = requests.get(url)
            f.write(response.content)
            f.close()

