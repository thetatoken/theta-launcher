# theta-launcher

Python script to download the latest mainnet snapshot and launch the Theta node

### Usage

Launch Theta with the following command. The parameter `password` is optional. If it is not provided, the Theta node will ask the user to enter the password manually. The script should detect whether there is a snapshot file under the specified config folder. If the snapshot does not exist, it will download the latest mainnet snapshot before launching the Theta node.

```
./theta_launcher.py path/to/config/folder [password]
```
