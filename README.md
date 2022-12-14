# PyMacnet

PyMacNet provides a channel level interface for communication and control of Maccor cyclers via MacNet.

## Running

See `examples/` to see instances of how to use the code for various tasks.

Note that the MaccorInterface class instance must receive a config dictionary on initialization. In the example code these are read from a JSON file:

- `channel` -> The channel to be targeted for all operations.
- `test` -> The test name to be used for any tests started. If left blank, Maccor will generate a unique random name for any started tests. Note that Maccor requires unique test names for each test.
- `test_procedure` -> The test procedure to be used, if starting a test with a procedure. Not needed with direct control.
- `c_rate_ah` -> The capacity value to be referenced when setting "C" values within the maccor schedule. Units of amp-hours. Ignored if not used anywhere in the test.
- `v_max_safety_limit_v` -> Upper voltage safety limit for the channel. Units of volts.
- `v_min_safety_limit_v` -> Lower voltage safety limit for the channel. Units of volts.
- `i_max_safety_limit_a` -> Upper current safety limit for the channel. Units of amps.
- `i_min_safety_limit_a` -> Lower current safety limit for the channel. Units of amps.
- `server_ip` -> The IP address of the Maccor server. Use 127.0.0.1 if running on the same machine as the server.
- `json_server_port` -> The port to communicate through with JSON commands. Default set to 57570.
- `tcp_server_port` -> The port to communicate through with TCP commands. Default set to 57560.
- `msg_buffer_size` -> Max buffer size for reading data back from Maccor server.

- `v_max_v` -> Upper voltage limit used for charge/CV limits. Units of volts. Only used with direct control.
- `v_min_v` -> Lower votage limit used for discharge limit. Units of volts. Only used with direct control.
- `data_record_time_s` -> How often data points are taken during direct control tests. Zero turns off. Used only for direct control.
- `data_record_voltage_delta_vbys` -> The dV/dt at which data points are taken during direct control tests. Zero disables. Used only for direct control.
- `data_record_current_delta_abys` -> The dI/dt at which data points are taken during direct control tests. Zero disables. Used only for direct control.


## Install

Navigate to the repo directory and run the following command:

```
pip install .
```

## Tests

Navigate to the repo directory and run the following command:

```
pip install .
```
