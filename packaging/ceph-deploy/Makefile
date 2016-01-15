srpm_repo = http://192.168.2.65/testing/EayunOBS/base_srpm
base_srpm = ceph-deploy-1.5.28-0.src.rpm
spec_file = ceph-deploy.spec

sources:
	mv $(spec_file) $(spec_file).new
	wget "$(srpm_repo)/$(base_srpm)" && \
	rpm2cpio $(base_srpm) | cpio -idmv && \
	rm -f $(spec_file) && \
	mv $(spec_file).new $(spec_file) && \
	rm -f $(base_srpm)
