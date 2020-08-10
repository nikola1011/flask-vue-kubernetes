## Represents the chaostoolkit experiments to be executed on this application
This folder holds JSON notation experiments that are used by [Chaostoolkit OpenAPI convention](https://chaostoolkit.org/) to introduce the chaos into the deployed Kubernetes application by empowering ["The principles of chaos engineering"](http://principlesofchaos.org/?lang=ENcontent).

### Install chaostoolkit

Use pip:
```pip install -U chaostoolkit```

Check for valid instalation:
```chaos --version```

Install Kubernetes plugin:
```chaos discover chaostoolkit-kubernetes```

See the [official repository](https://github.com/chaostoolkit/chaostoolkit) for detailed explanations

### Running experiments

In order to run the experiment execute:
```chaos run <experiment-file-path>```

For example run:
```chaos run sanity-check.json```
experiment, that will check if all the microservices are healthy and if all pods are in 'Running' status.