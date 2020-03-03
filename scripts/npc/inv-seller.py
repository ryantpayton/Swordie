# Custom NPC script used for @sell player command
# Author: Clueless Cow

from net.swordie.ms.loaders import ItemData
from net.swordie.ms.constants import ItemConstants

def disposeAll():
    sm.dispose()
    chr.dispose()

def sellItemsFromEquipmentTab():
    # query inv info
    eqInventory = chr.getEquipInventory()
    eqs = eqInventory.getItems()

    # empty inv
    if len(eqs) == 0:
        sm.sendSayOkay("You have no item to sell")
        disposeAll()
        return

    # has at least 1 item in inv
    # sellingItems = []
    if len(eqs) == 1:
        # only has 1 item, proceed to ask for confirmation
        sellingItems = list(eqs)
        _itemId = eqs.get(0).getItemId()
        confirmed = sm.sendAskYesNo("Are you sure you want to sell #i{}# #z{}#".format(_itemId, _itemId))
    else:
        # has more than 1 item, prompt mode selection
        optionList = "Please select what you want to sell in your EQUIPMENT tab:\r\n#L1##rEverything#k#l\r\n#L2##gSell between selected items#k#l\r\n#L3#Maybe later#l\r\n"
        option = sm.sendNext(optionList)
        if option:
            if option == 1:
                # sell everything
                sellingItems = list(eqs)
                confirmed = sm.sendAskYesNo("Are you sure you want to sell #rEVERYTHING#k in your Equipment inventory?")
            if option == 2:
                # sell from/to
                def sortByBagIndex(item):
                    return item.getBagIndex()
                sortedItems = list(eqs)
                sortedItems.sort(key=sortByBagIndex)
                itemListTemplate = "This option will sell all available items between STARTING item and ENDING item.\r\nPlease select #r<order>#k item:\r\n"
                for item in sortedItems:
                    itemListTemplate += "#L{}##i{}# #z{}##l\r\n".format(item.getBagIndex(), item.getItemId(), item.getItemId())
                startIndex = sm.sendNext(itemListTemplate.replace("<order>", "STARTING"))
                endIndex = sm.sendNext(itemListTemplate.replace("<order>", "ENDING"))
                if startIndex > endIndex:
                    startIndex, endIndex = endIndex, startIndex
                def isInRange(item):
                    bagIndex = item.getBagIndex()
                    return bagIndex >= startIndex and bagIndex <= endIndex
                sellingItems = filter(isInRange, sortedItems)
                soldItemsTemplate = "You will sell the following items:\r\n"
                for item in sellingItems:
                    soldItemsTemplate += "#i{}# #z{}#\r\n".format(item.getItemId(), item.getItemId(), item.getBagIndex())
                confirmed = sm.sendAskYesNo(soldItemsTemplate)
        else:
            # 'maybe later' option / no response
            disposeAll()
            return
    # finish asking for selling items, proceed to actually sell it
    if not confirmed:
        sm.sendSayOkay("Thank you for using my service")
        disposeAll()
        return

    # player confirmed
    totalMesos = 0
    for item in sellingItems:
        cost = 0
        id = item.getItemId()
        quantity = item.getQuantity()
        if ItemConstants.isEquip(id):
            cost = item.getPrice() * quantity
        else:
            info = ItemData.getItemInfoByID(id)
            if info:
                cost = info.getPrice() * quantity
            else:
                continue
        totalMesos += cost

    if chr.canAddMoney(totalMesos):
        # remove item from inv
        for soldItem in sellingItems:
            sm.consumeItem(soldItem.getItemId())
        # add money
        chr.addMoney(totalMesos)
        sm.sendSayOkay("You've received {} mesos. Thank you for using my service!".format(totalMesos))
        disposeAll()
        return
    else:
        sm.sendSayOkay("#rYou've reached maximum meso cap.#k Please deposit at least {} mesos and run the command again!".format(totalMesos))
        disposeAll()
        return

sellItemsFromEquipmentTab()
