import deploymentFunctions as depfunc 

storageAccountName = 'tfbkendabc123x'  
storageContainerName = 'tfcontainer'  
resourceGroupName = 'pipeline-resources'  
resourceGroupLocation = 'westus'  

#First delete the storage container within the storage account
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest#az-storage-container-create
#deleteStorageContainerCommand = "az storage container delete --account-name " + storageAccountName + " --name " + storageContainerName 
#print("deleteStorageContainerCommand is: ", deleteStorageContainerCommand)
#depfunc.runShellCommand(deleteStorageContainerCommand)  

#Then delete the storage account
#https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-cli
deleteStorageAccountCommand = "az storage account delete --name " + storageAccountName + " --resource-group " + resourceGroupName  
print("deleteStorageAccountCommand is: ", deleteStorageAccountCommand)
depfunc.runShellCommand(deleteStorageAccountCommand)  
