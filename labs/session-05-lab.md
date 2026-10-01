# Session 5 lab — A virtual network, then three kinds of endpoint

**Time:** 30 minutes
**Objectives practiced:** 2.2.5, 2.2.6, 3.3.2
**You need:** Cloud Shell for Part A, or the no-cost trace. Part B is paper.

---

## Part A — Two subnets (15 minutes)

In [Cloud Shell](https://shell.azure.com), bash mode, Azure CLI.

1. Create the group. Use the region the instructor writes on the board in place of `REGION`.

```bash
az group create --name az900-s05-lab --location REGION --tags course=az900 session=s05
```

2. Create a network with one subnet.

```bash
az network vnet create \
  --resource-group az900-s05-lab \
  --name s05-vnet \
  --address-prefix 10.50.0.0/16 \
  --subnet-name app \
  --subnet-prefix 10.50.1.0/24
```

3. Add the second subnet.

```bash
az network vnet subnet create \
  --resource-group az900-s05-lab \
  --vnet-name s05-vnet \
  --name data \
  --address-prefix 10.50.2.0/24
```

4. Show what you made.

```bash
az network vnet show --resource-group az900-s05-lab --name s05-vnet --output table
az network vnet subnet list --resource-group az900-s05-lab --vnet-name s05-vnet --output table
```

5. In the portal, open resource group `az900-s05-lab` and find `s05-vnet`. You should see subnets `app` and `data`.
6. Delete the group before you leave.

```bash
az group delete --name az900-s05-lab --yes --no-wait
```

### No-cost path

Do not run the commands. For each command, write the noun it creates (group, virtual network, subnet) and read the matching section of
[virtual networks overview](https://learn.microsoft.com/en-us/azure/virtual-network/virtual-networks-overview).
The instructor shows a finished VNet blade, or the command output, on the projector.

## Part B — Public, private, or service endpoint (15 minutes)

Write **public**, **private endpoint**, or **service endpoint**.

1. A storage account is reached at a public address from the internet.
2. A database gets a network interface and a private IP inside your subnet. Clients in the virtual network use that IP.
3. Traffic from a subnet to a storage account stays on the Microsoft backbone, and the storage account still uses its public address. You restrict the account to that subnet.
4. You want the PaaS resource to have an address that looks like the rest of your private range.
5. A virtual machine's public IP, with port 443 allowed.
6. You turn off public network access on a service and allow only the private address in your virtual network.
7. There is no new network interface in your subnet. The service endpoint is a route and an identity for the subnet, toward the service's public endpoint.
8. A partner on the internet must reach a website that is intentionally public.
9. A compliance note says the data service must not be accessed through a public IP from your application subnet.

<div class="pagebreak"></div>

## Instructor key

### Part A

Group `az900-s05-lab`, VNet `s05-vnet` `10.50.0.0/16`, subnets `app` `10.50.1.0/24` and `data` `10.50.2.0/24`. Delete the group. `--no-wait` means the delete may still be running when the quiz starts; that is fine if it was issued.

Cloud Shell may ask to create a storage account the first time. That account is Cloud Shell's, not the lab. Do not delete the `cloud-shell-storage` group by mistake.

### Part B

1. Public
2. Private endpoint
3. Service endpoint
4. Private endpoint
5. Public
6. Private endpoint
7. Service endpoint
8. Public
9. Private endpoint

Row 9 is private endpoint, not service endpoint, because the requirement is about not using a public IP. A service endpoint still targets the public address.
