import deploymentFunctions as depfunc 

storageAccountName = 'tfbkendabc123x'  
storageContainerName = 'tfcontainer'  
resourceGroupName = 'pipeline-resources'  
resourceGroupLocation = 'westus'  
keyVaultName = 'testvlt789' 
keyName = 'demoStorageKey' 

#First create storage account
#https://docs.microsoft.com/en-us/azure/storage/common/storage-account-create?tabs=azure-cli
createStorageAccountCommand = "az storage account create --name " + storageAccountName + " --resource-group " + resourceGroupName + " --location " + resourceGroupLocation + " --sku Standard_LRS   --encryption-services blob"
print("createStorageAccountCommand is: ", createStorageAccountCommand)
depfunc.runShellCommand(createStorageAccountCommand)  

getAccountKeyCommand = "az storage account keys list --resource-group " + resourceGroupName + " --account-name " + storageAccountName + " --query [0].value -o tsv "  
#print("getAccountKeyCommand is: ", getAccountKeyCommand)  
accountKey = depfunc.getAccountKey(getAccountKeyCommand)  
#print("accountKey is: ", accountKey)  

#Then create a storage container within the storage account  
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest
# #https://docs.microsoft.com/en-us/cli/azure/storage/container?view=azure-cli-latest#az-storage-container-create
createStorageContainerCommand = "az storage container create -n " + storageContainerName + " --fail-on-exist --account-name " + storageAccountName + " --account-key " + accountKey  
print("createStorageContainerCommand is: ", createStorageContainerCommand)
depfunc.runShellCommand(createStorageContainerCommand)  

#Then add the storage account key to the keyvault so that the key can be used by a pipeline.  
createSecretCommand = 'az keyvault secret set --vault-name ' + keyVaultName + ' --name ' + keyName + ' --value ' + accountKey 
#print("createSecretCommand is: ", createSecretCommand)    
depfunc.runShellCommand(createSecretCommand)    
  
