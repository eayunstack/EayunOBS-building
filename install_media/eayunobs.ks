lang zh_CN.utf-8
keyboard us
timezone Asia/Shanghai
selinux --disable
firewall --disabled
clearpart --all --initlabel
zerombr
services --enabled=pcsd

%packages
@Core
@Base
@Ceph Rados Gateway
%end

%post
# allow nonlocal binding for HAProxy
echo 'net.ipv4.ip_nonlocal_bind=1' >> /etc/sysctl.conf

# set default password for hacluster user
echo 'hacluster:$6$EayunOBS$urxceAgu/OlKHTm/JQyl/LBuVcLI8u.emVy.lIAs08zzZTKDmsxXTBoG.EfDjYY4oCegcbM0QKoJ8dszsHYpL/' | chpasswd --encrypted
%end

reboot --eject
