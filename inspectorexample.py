import mmapi
from mmRemote import *
import mm

remote = mmRemote()
remote.connect()


mm.begin_tool(remote,'inspector')
# optional parameters:    (note: I need to set replaceType first - otherwise it uses default FlatFill
mm.set_toolparam(remote, 'replaceType', 2) # Integer: MinimalFill = 0, FlatFill = 1, SmoothFill = 2
mm.set_toolparam(remote, 'smallComponentThreshold', 0.002) # Float

# AutoRepairAll:
mm.tool_utility_command(remote, "repairAll")

# to leave Inspector:
mm.accept_tool(remote)

remote.shutdown()
