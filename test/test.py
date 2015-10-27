import os
import requests

from qubell.api.testing import *

@environment({
    "default": {}
})
class KubernetesOnMesosDevTestCase(BaseComponentTestCase):
    name = "component-kubernetes-mesos"
    #meta = os.path.realpath(os.path.join(os.path.dirname(__file__), '../meta.yml')) 
    destroy_interval = int(os.environ.get('DESTROY_INTERVAL', 1000*60*60*2))
    apps = [
       {"name": name,
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../%s.yml' % name)),
        "settings": {"destroyInterval": destroy_interval}
       },
       {"name": "Mesos",
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../mesos.yml')),
        "launch": False 
       },
       {"name": "Zookeeper",
        "url": "https://raw.github.com/qubell-bazaar/component-zookeeper-dev/1.2-41p/component-zookeeper-dev.yml",
        "launch": False 
       },
       {"name": "VM",
        "file": os.path.realpath(os.path.join(os.path.dirname(__file__), '../vm.yml')),
        "launch": False
       }
    ]

    @classmethod
    def timeout(cls):
        return 60
   
    @instance(byApplication=name)
    def test_kube_instans(self, instance):
        url = instance.returnValues['kubernetes.kube-ui']
        resp = requests.get(url, verify=False, allow_redirects=False)
        assert resp.status_code == 301
