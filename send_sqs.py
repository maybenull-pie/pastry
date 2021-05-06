# example sqs send
from pastry.core.queue import Queue, Queues
from pastry.core.event import ISqsHappend

q = Queue(name=Queues.POLICY)
q.send(event=ISqsHappend({'Foo': 'Barz'}))

