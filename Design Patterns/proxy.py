import time


class Producer:
    """ define the 'resource intensive obj to instantiate! """
    def produce(self):
        print("Producer is working hard!")

    def meet(self):
        print("Producer has time to meet you now")


class Proxy:
    """ Define the 'relatively resource intensive' proxy to instantiate as a middleman! """
    def __init__(self):
        self.occupied = "No"
        self.producer = None

    def produce(self):
        # checking availability of producer
        print("Artist checking if produce is available....")

        if self.occupied == "No":
            # if the producer is available, create a producer object
            self.producer = Producer()
            time.sleep(2)
            # Make the meet possible
            self.producer.meet()

        else:
            # otherwise don't instantiate a producer
            time.sleep(2)
            print("Producer is busy!")


# instantiate the Proxy
p = Proxy()
# Make thr proxy: Artist produce until Producer is available
p.produce()
# Change the state to "occupied"
p.occupied = "Yes"
# Make the producer available
p.produce()
