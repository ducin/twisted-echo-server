import unittest
import multiprocessing
import time
import server, client

class MainTest (unittest.TestCase):
    """
    This test runs the server in a shell subprocess and after a second
    it runs the client in another shell subprocess. Afterwards, it kills
    both processes and run assertions on the output.
    The testing is a little bit brutal.
    """
    def test_run(self):
        sp = multiprocessing.Process(target=server.run, args=())
        cp = multiprocessing.Process(target=client.run, args=())
        sp.start()
        time.sleep(1)
        cp.start()
        time.sleep(1)
        sp.terminate()

        f = open('client.log')
        output = [line.rstrip() for line in f.readlines()]
        f.close()
        print output
        self.assertEqual(output, ['OUT:hello', 'IN:hello', 'OUT:from', 'IN:from', 'OUT:twisted', 'IN:twisted', 'OUT:client', 'IN:client', 'OUT:exit', 'IN:exit'])
