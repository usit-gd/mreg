from django.urls import path, re_path

from . import views

urlpatterns = [
    path('cnames/', views.CnameList.as_view()),
    path('cnames/<name>', views.CnameDetail.as_view()),
    path('dhcphosts/v4/all', views.DhcpHostsAllV4.as_view()),
    path('dhcphosts/v6/all', views.DhcpHostsAllV6.as_view()),
    path('dhcphosts/v6byv4/<ip>/<range>', views.DhcpHostsV4ByV6.as_view()),
    path('dhcphosts/v6byv4/', views.DhcpHostsV4ByV6.as_view()),
    path('dhcphosts/<ip>/<range>', views.DhcpHostsByRange.as_view()),
    path('hinfopresets/', views.HinfoPresetList.as_view()),
    path('hinfopresets/<pk>', views.HinfoPresetDetail.as_view()),
    path('hosts/', views.HostList.as_view()),
    path('hosts/<pk>', views.HostDetail.as_view()),
    path('ipaddresses/', views.IpaddressList.as_view()),
    path('ipaddresses/<pk>', views.IpaddressDetail.as_view()),
    path('mxs/', views.MxList.as_view()),
    path('mxs/<pk>', views.MxDetail.as_view()),
    path('naptrs/', views.NaptrList.as_view()),
    path('naptrs/<pk>', views.NaptrDetail.as_view()),
    path('nameservers/', views.NameServerList.as_view()),
    path('nameservers/<pk>', views.NameServerDetail.as_view()),
    path('ptroverrides/', views.PtrOverrideList.as_view()),
    path('ptroverrides/<pk>', views.PtrOverrideDetail.as_view()),
    path('sshfps/', views.SshfpList.as_view()),
    path('sshfps/<pk>', views.SshfpDetail.as_view()),
    path('srvs/', views.SrvList.as_view()),
    path('srvs/<pk>', views.SrvDetail.as_view()),
    path('networks/', views.NetworkList.as_view()),
    path('networks/ip/<ip>', views.network_by_ip),
    path('networks/<ip>/<range>', views.NetworkDetail.as_view()),
    path('networks/<ip>/<range>/first_unused', views.network_first_unused),
    path('networks/<ip>/<range>/ptroverride_list', views.network_ptroverride_list),
    path('networks/<ip>/<range>/ptroverride_host_list', views.network_ptroverride_host_list),
    path('networks/<ip>/<range>/reserved_list', views.network_reserved_list),
    path('networks/<ip>/<range>/used_count', views.network_used_count),
    path('networks/<ip>/<range>/used_list', views.network_used_list),
    path('networks/<ip>/<range>/used_host_list', views.network_used_host_list),
    path('networks/<ip>/<range>/unused_count', views.network_unused_count),
    path('networks/<ip>/<range>/unused_list', views.network_unused_list),
    path('txts/', views.TxtList.as_view()),
    path('txts/<pk>', views.TxtDetail.as_view()),
    path('zones/', views.ZoneList.as_view()),
    re_path(r'^zones/(?P<name>(\d+/)?[^/]+)$', views.ZoneDetail.as_view()),
    re_path(r'^zones/(?P<name>(\d+/)?[^/]+)/delegations/$', views.ZoneDelegationList.as_view()),
    re_path(r'^zones/(?P<name>(\d+/)?[^/]+)/delegations/(?P<delegation>(.*))', views.ZoneDelegationDetail.as_view()),
    re_path(r'^zones/(?P<name>(\d+/)?[^/]+)/nameservers$', views.ZoneNameServerDetail.as_view()),
    re_path(r'^zonefiles/(?P<name>(\d+/)?[^/]+)', views.ZoneFileDetail.as_view()),
    path('history/', views.ModelChangeLogList.as_view()),
    path('history/<table>/<pk>', views.ModelChangeLogDetail.as_view()),
]
