Python cinsole script for Warframe.
Displays Void trader Baro Ki’Teer timers arrive/leave.
In which relay he will arrive and the items that he trades - when arrives.
You can add new items in "items.json" file, using the same format.

{
    ...
    "/Lotus/StoreItems/Types/Game/KubrowPet/Eggs/KubrowEgg": "Kubrow Egg",
    ...
}

You will see an error if DE will add some new items in game, so you could add them,
by yourself.

All data - from "worldState.php"

So, you need python 3 and modules:
os, time, requests, json, pickle, datetime

Created mostly for 
