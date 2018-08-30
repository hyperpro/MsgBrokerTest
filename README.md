# Msgbroker Test
 A HelloWorld Program For A Msgbroker.
 
## Dependency

### MacOS
1. Python 3
>  brew install python3

2. Pika
>  pip install pika

3. RabbitMQ
>  brew install rabbitmq

4. MongoDB
> brew install mongodb

### Debian/Ubuntu

## How to Run

### Debian/Ubuntu 18.04
1. Start All Service
> service rabbitmq-server start

2. Initial Receiver
> python Receiver.py

3. Run Sender
> python SenderStart.py

The results of the requests is on the commandline.
 
## Edit File
1. Scheduler Type

Users can change the scheduler type in the SenderStart.py. Fill the variable 'Scheduler' with the scheduler type

2. Request's File

Users can link your file with nb-delay of requets in SenderStart.py. Fill the variable 'RequestsNB_FILE' with the file address

3. Results

Users can see the results in the commandline windows of Receiver.py.



