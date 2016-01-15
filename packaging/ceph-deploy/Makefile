srpm_repo = http://download.ceph.com/rpm-firefly/el7/SRPMS
base_srpm = ceph-deploy-1.5.28-0.src.rpm
spec_file = ceph-deploy.spec

sources:
	mv $(spec_file) $(spec_file).new
	wget "$(srpm_repo)/$(base_srpm)" && \
	rpm2cpio $(base_srpm) | cpio -idmv && \
	rm -f $(spec_file) && \
	mv $(spec_file).new $(spec_file) && \
	rm -f $(base_srpm)
