import deploymentFunctions as depfunc 

storageAccountName = 'tfbkendabc123x'  
storageContainerName = 'tfcontainer'  
resourceGroupName = 'pipeline-resources'  
resourceGroupLocation = 'westus'  

#First create storage account
#https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-cli
createStorageAccountCommand = "az storage account create --name " + storageAccountName + " --resource-group " + resourceGroupName + " --location " + resourceGroupLocation + " --sku Standard_RAGRS --kind StorageV2"
print("createStorageAccountCommand is: ", createStorageAccountCommand)
depfunc.runShellCommand(createStorageAccountCommand)  

#Then create a storage container within the storage account  
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest#az-storage-container-create
#createStorageContainerCommand = "az storage container create -n " + storageContainerName + " --fail-on-exist --account-name " + storageAccountName
#print("createStorageContainerCommand is: ", createStorageContainerCommand)
#depfunc.runShellCommand(createStorageContainerCommand)  
