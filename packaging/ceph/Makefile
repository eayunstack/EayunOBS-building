srpm_repo = http://192.168.2.65/testing/EayunOBS/base_srpm
base_srpm = ceph-0.80.7-0.4.el7.src.rpm
spec_file = ceph.spec

sources:
	mv $(spec_file) $(spec_file).new
	wget "$(srpm_repo)/$(base_srpm)" && \
	rpm2cpio $(base_srpm) | cpio -idmv && \
	rm -f $(spec_file) && \
	mv $(spec_file).new $(spec_file) && \
	rm -f $(base_srpm)
