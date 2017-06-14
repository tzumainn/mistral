# Copyright 2014 - Mirantis, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import mock

from mistral.actions.openstack import actions
from oslotest import base


class FakeEndpoint(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


class OpenStackActionTest(base.BaseTestCase):
    @mock.patch.object(actions.NovaAction, '_get_client')
    def test_nova_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "servers.get"
        action_class = actions.NovaAction
        action_class.client_method_name = method_name
        params = {'server': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().servers.get.called)
        mocked().servers.get.assert_called_once_with(server="1234-abcd")

    @mock.patch.object(actions.GlanceAction, '_get_client')
    def test_glance_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "images.delete"
        action_class = actions.GlanceAction
        action_class.client_method_name = method_name
        params = {'image': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().images.delete.called)
        mocked().images.delete.assert_called_once_with(image="1234-abcd")

    @mock.patch.object(actions.KeystoneAction, '_get_client')
    def test_keystone_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "users.get"
        action_class = actions.KeystoneAction
        action_class.client_method_name = method_name
        params = {'user': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().users.get.called)
        mocked().users.get.assert_called_once_with(user="1234-abcd")

    @mock.patch.object(actions.HeatAction, '_get_client')
    def test_heat_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "stacks.get"
        action_class = actions.HeatAction
        action_class.client_method_name = method_name
        params = {'id': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().stacks.get.called)
        mocked().stacks.get.assert_called_once_with(id="1234-abcd")

    @mock.patch.object(actions.NeutronAction, '_get_client')
    def test_neutron_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "show_network"
        action_class = actions.NeutronAction
        action_class.client_method_name = method_name
        params = {'id': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().show_network.called)
        mocked().show_network.assert_called_once_with(id="1234-abcd")

    @mock.patch.object(actions.CinderAction, '_get_client')
    def test_cinder_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "volumes.get"
        action_class = actions.CinderAction
        action_class.client_method_name = method_name
        params = {'volume': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().volumes.get.called)
        mocked().volumes.get.assert_called_once_with(volume="1234-abcd")

    @mock.patch.object(actions.CeilometerAction, '_get_client')
    def test_ceilometer_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "alarms.get"
        action_class = actions.CeilometerAction
        action_class.client_method_name = method_name
        params = {'alarm_id': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().alarms.get.called)
        mocked().alarms.get.assert_called_once_with(alarm_id="1234-abcd")

    @mock.patch.object(actions.TroveAction, '_get_client')
    def test_trove_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "instances.get"
        action_class = actions.TroveAction
        action_class.client_method_name = method_name
        params = {'instance': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().instances.get.called)
        mocked().instances.get.assert_called_once_with(instance="1234-abcd")

    @mock.patch.object(actions.IronicAction, '_get_client')
    def test_ironic_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "node.get"
        action_class = actions.IronicAction
        action_class.client_method_name = method_name
        params = {'node': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().node.get.called)
        mocked().node.get.assert_called_once_with(node="1234-abcd")

    @mock.patch.object(actions.BaremetalIntrospectionAction, '_get_client')
    def test_baremetal_introspector_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "get_status"
        action_class = actions.BaremetalIntrospectionAction
        action_class.client_method_name = method_name
        params = {'uuid': '1234'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().get_status.called)
        mocked().get_status.assert_called_once_with(uuid="1234")

    @mock.patch.object(actions.MistralAction, '_get_client')
    def test_mistral_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "workflows.get"
        action_class = actions.MistralAction
        action_class.client_method_name = method_name
        params = {'name': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().workflows.get.called)
        mocked().workflows.get.assert_called_once_with(name="1234-abcd")

    @mock.patch.object(actions.SwiftAction, '_get_client')
    def test_swift_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "get_object"
        action_class = actions.SwiftAction
        action_class.client_method_name = method_name
        params = {'container': 'foo', 'object': 'bar'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().get_object.called)
        mocked().get_object.assert_called_once_with(container='foo',
                                                    object='bar')

    @mock.patch.object(actions.ZaqarAction, '_get_client')
    def test_zaqar_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "queue_messages"
        action_class = actions.ZaqarAction
        action_class.client_method_name = method_name
        params = {'queue_name': 'foo'}
        action = action_class(**params)
        action.run(mock_ctx)

        mocked().queue.assert_called_once_with('foo')
        mocked().queue().messages.assert_called_once_with()

    @mock.patch.object(actions.BarbicanAction, '_get_client')
    def test_barbican_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "orders_list"
        action_class = actions.BarbicanAction
        action_class.client_method_name = method_name
        params = {'limit': 5}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().orders_list.called)
        mocked().orders_list.assert_called_once_with(limit=5)

    @mock.patch.object(actions.DesignateAction, '_get_client')
    def test_designate_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "domain.get"
        action_class = actions.DesignateAction
        action_class.client_method_name = method_name
        params = {'domain': 'example.com'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().domain.get.called)
        mocked().domain.get.assert_called_once_with(domain="example.com")

    @mock.patch.object(actions.MagnumAction, '_get_client')
    def test_magnum_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "baymodels.get"
        action_class = actions.MagnumAction
        action_class.client_method_name = method_name
        params = {'id': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().baymodels.get.called)
        mocked().baymodels.get.assert_called_once_with(id="1234-abcd")

    @mock.patch.object(actions.MuranoAction, '_get_client')
    def test_murano_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "categories.get"
        action_class = actions.MuranoAction
        action_class.client_method_name = method_name
        params = {'category_id': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().categories.get.called)
        mocked().categories.get.assert_called_once_with(
            category_id="1234-abcd"
        )

    @mock.patch.object(actions.TackerAction, '_get_client')
    def test_tacker_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "show_vim"
        action_class = actions.TackerAction
        action_class.client_method_name = method_name
        params = {'vim_id': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().show_vim.called)
        mocked().show_vim.assert_called_once_with(
            vim_id="1234-abcd"
        )

    @mock.patch.object(actions.SenlinAction, '_get_client')
    def test_senlin_action(self, mocked):
        mock_ctx = mock.Mock()
        action_class = actions.SenlinAction
        action_class.client_method_name = "get_cluster"
        action = action_class(cluster_id='1234-abcd')

        action.run(mock_ctx)

        self.assertTrue(mocked().get_cluster.called)

        mocked().get_cluster.assert_called_once_with(
            cluster_id="1234-abcd"
        )

    @mock.patch.object(actions.AodhAction, '_get_client')
    def test_aodh_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "alarm.get"
        action_class = actions.AodhAction
        action_class.client_method_name = method_name
        params = {'alarm_id': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().alarm.get.called)
        mocked().alarm.get.assert_called_once_with(alarm_id="1234-abcd")

    @mock.patch.object(actions.GnocchiAction, '_get_client')
    def test_gnocchi_action(self, mocked):
        mock_ctx = mock.Mock()
        method_name = "metric.get"
        action_class = actions.GnocchiAction
        action_class.client_method_name = method_name
        params = {'metric_id': '1234-abcd'}
        action = action_class(**params)
        action.run(mock_ctx)

        self.assertTrue(mocked().metric.get.called)
        mocked().metric.get.assert_called_once_with(metric_id="1234-abcd")
