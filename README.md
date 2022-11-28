# Readme

Rich-json-logs is a command line tool written in Python that allows to visualize logs in a tabular format. 

By default it tries to parse json logs and extract the relevant columns passed as options. If a list of columns is not provided it uses the default value `@timestamp,log.level,message`. You can also use jsonpath to extract nested json columns (even with `.` in the column name) like `@timestamp,log.logger,$.'log.origin'.'file.name',message`. In case a column is not present in a json line, the value for that column will be filled with `-` instead.

In case the logs are not json, it will avoid parsing the text and insert it as the last column of the table.

You can either use the script to visualize logs from a file on your local filesystem with ndjson format (1 json per line)

```bash
python main.py -i sample.log
```

 or otherwise read from Stdin using a pipe command

```bash
cat sample.log | python main.py | less -r
```

In the first example, the python script already comes with a pager, while in the second example you need to use an external pager. Here `less -r` supports colored output.

## Install
You need to install some required libraries that are listed on requirements.txt

```bash
pip install -r requirements.txt
```

## Help
In order to see the list of supported options, you can issue the following command

```bash
› python main.py --help                          
Usage: main.py [OPTIONS]

Options:
  -i, --input-path TEXT  Input path
  -c, --columns TEXT     Columns to filter
  --help                 Show this message and exit.
```

## Kubectl plugin
Rich-json-logs
can be used as a kubectl plugin by wrapping it in a bash script

```bash
#!/bin/bash
/usr/local/bin/kubectl logs $1 -n $2 --context $3 \
        | python main.py \
        | less -r
```

I have attached the following script at `bin/kubectl-rich.sh`. In order to use it as a kubectl plugin, the following script needs to be added to the PATH environment variable.

Finally it can be used as following

```bash
kubectl rich <pod-name> <namespace> <context>
```

## K9s plugin
You can also use the kubectl plugin here provided as a [K9s plugin](https://k9scli.io/topics/plugins/) by adding the following entry to the `~/.k9s/plugin.xml` file. Once you are inside k9s on the Pod view, you can type `ctrl+j` to use colored-logs to visualize logs in a tabular form. 

```bash
plugin:
  rich:
    shortCut: Ctrl-J
    confirm: false
    description: "Logs (rich)"
    scopes:
      - po
    command: kubectl
    background: false
    args:
      - rich
      - $NAME
      - $NAMESPACE
      - $CONTEXT
```
