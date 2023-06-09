###########################################################
### Default configuration block when working with Azure ###
###########################################################
terraform {
  # Provide configuration details for Terraform
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~>3.49"
    }
  }

  # configuration to update the infrastructure.
  # Link: https://learn.microsoft.com/en-us/azure/developer/terraform/store-state-in-azure-storage?tabs=azure-cli
  # Note.- Before using this block, is important that the resource group, storage account and container ARE DEPLOYED.
  backend "azurerm" {
    resource_group_name  = "dip-prd-master-rg"
    storage_account_name = "dipprdmasterst"
    container_name       = "dip-prd-asdlgen2-fs-config"
    key                  = "ike-dev-58uf76-rg/terraform.tfstate"

  }
}


# provide configuration details for the Azure terraform provider
provider "azurerm" {
  features {
    key_vault {
      purge_soft_delete_on_destroy = true
    }
  }
}



# For naming conventions please refer to:
# https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/resource-name-rules

data "azuread_client_config" "current" {}


###########################################################
###################  Resource Group #######################
###########################################################
resource "azurerm_resource_group" "rg" {
  location = var.location
  name     = "${var.default_prefix}-${var.environment}-${var.random_id}-rg"
  # tags = {
    # owner       = var.owner
    # environment = var.environment

  # }
}


###########################################################
###################  Storage Account ######################
###########################################################
resource "azurerm_storage_account" "storageaccount" {
  name = "${var.default_prefix}${var.environment}${var.random_id}st" # Between 3 to 24 characters and
                                                                     # UNIQUE within Azure
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  account_kind             = "StorageV2"
  is_hns_enabled           = "true"

  tags = {
    owner       = var.owner
    environment = var.environment
  }
}

###########################################################
########  Azure Storage Data Lake Gen2 Filesystem #########
###########################################################
resource "azurerm_storage_data_lake_gen2_filesystem" "myasdlgen2replica1" {
  name               = "${var.default_prefix}-${var.environment}-landing-zone"
  storage_account_id = azurerm_storage_account.storageaccount.id

  properties = {
    hello = "aGVsbG8="
  }
}

###########################################################
##############  Azure Data Factory Engine #################
###########################################################
resource "azurerm_data_factory" "datafactory" {
  name = "${var.default_prefix}-${var.environment}-${var.random_id}-datafactory" # Between 3 to 63 characters and
                                                                                 # UNIQUE within Azure
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location

  # Create a Managed Identity feature
  identity {
    type = "SystemAssigned"
  }

  tags = {
    owner       = var.owner
    environment = var.environment
  }

}

###########################################################
#################  Container Registry #####################
###########################################################

resource "azurerm_container_registry" "acr" {
  name                = "${var.default_prefix}${var.environment}${var.random_id}acr"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Standard"
  admin_enabled       = true
}


###########################################################
############  Flexible Postgresql Database ################
###########################################################

resource "azurerm_postgresql_flexible_server" "example" {
  name                   = "${var.default_prefix}-${var.environment}-psql"
  resource_group_name    = azurerm_resource_group.rg.name
  location               = azurerm_resource_group.rg.location
  version                = "14"
  administrator_login    = var.user_psql
  administrator_password = var.pwd_psql

  storage_mb = 32768

  sku_name = "B_Standard_B1ms"
}

