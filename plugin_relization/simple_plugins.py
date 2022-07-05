#!/usr/bin/env python
import fire
import pkgutil
import importlib

def find_and_run_plugins(plugin_prefix):
    plugins = {}

    # Detecting and loading plugins
    print(f"Discovering plugins with prefix: {plugin_prefix}")
    # pkgutil.iter_modules() returnes all avaliable for current sys.path modules
    for _, name, _ in pkgutil.iter_modules():
        # if module starts with interesting prefix
        if name.startswith(plugin_prefix):
            # loading neccessary module and save it to dict
            module = importlib.import_module(name)
            plugins[name] = module
    # run plugins
    for name, module in plugins.items():
        print(f"Running plugin {name}")
        # runs plugin
        module.run()

if __name__ == "__main__":
    fire.Fire()
    

