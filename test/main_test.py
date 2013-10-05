import unittest
import subprocess
import time
import os, signal
# terminating subprocess: http://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true

class MainTest (unittest.TestCase):
    """
    This test runs the server in a shell subprocess and after a second
    it runs the client in another shell subprocess. Afterwards, it kills
    both processes and run assertions on the output.
    The testing is a little bit brutal.
    """
    def test_run(self):
        sp = subprocess.Popen('python server.py', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        time.sleep(1)
        cp = subprocess.Popen('python client.py', stdout=subprocess.PIPE, shell=True, preexec_fn=os.setsid)
        time.sleep(1)
        os.killpg(sp.pid, signal.SIGTERM)
        self.assertEqual(sp.stdout.readlines(), [])
        self.assertEqual(cp.stdout.readlines(), ['> hello\n', '< hello\n'])
