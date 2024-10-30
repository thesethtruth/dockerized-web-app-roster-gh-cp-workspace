provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "main" {
  name     = "simple-web-app-rg"
  location = "East US"
}

resource "azurerm_container_group" "frontend" {
  name                = "frontend-container-group"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"

  container {
    name   = "frontend"
    image  = "frontend:latest"
    cpu    = "0.5"
    memory = "1.5"

    ports {
      port     = 3000
      protocol = "TCP"
    }

    environment_variables = {
      REACT_APP_API_URL = "http://backend:8000"
    }
  }

  ip_address {
    type = "Public"
    ports {
      port     = 3000
      protocol = "TCP"
    }
  }
}

resource "azurerm_container_group" "backend" {
  name                = "backend-container-group"
  location            = azurerm_resource_group.main.location
  resource_group_name = azurerm_resource_group.main.name
  os_type             = "Linux"

  container {
    name   = "backend"
    image  = "backend:latest"
    cpu    = "0.5"
    memory = "1.5"

    ports {
      port     = 8000
      protocol = "TCP"
    }

    environment_variables = {
      DATABASE_URL = "sqlite:///./test.db"
    }
  }

  ip_address {
    type = "Public"
    ports {
      port     = 8000
      protocol = "TCP"
    }
  }
}

resource "azurerm_storage_account" "main" {
  name                     = "simplestorageacct"
  resource_group_name      = azurerm_resource_group.main.name
  location                 = azurerm_resource_group.main.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_container" "main" {
  name                  = "backend-storage"
  storage_account_name  = azurerm_storage_account.main.name
  container_access_type = "private"
}

resource "azurerm_storage_blob" "main" {
  name                   = "test.db"
  storage_account_name   = azurerm_storage_account.main.name
  storage_container_name = azurerm_storage_container.main.name
  type                   = "Block"
  source                 = "${path.module}/../backend/test.db"
}
