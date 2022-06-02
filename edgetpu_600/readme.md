
examples:
	bazel build $(BAZEL_BUILD_FLAGS) //coral/examples:two_models_one_tpu \
	                                 //coral/examples:two_models_two_tpus_threaded \
	                                 //coral/examples:model_pipelining \
	                                 //coral/examples:classify_image \
	                                 //coral/examples:detect_image \
	                                 //coral/examples:backprop_last_layer \
	                                 //coral/examples:bug
	mkdir -p $(EXAMPLES_OUT_DIR)
	cp -f $(BAZEL_OUT_DIR)/coral/examples/two_models_one_tpu \
	      $(BAZEL_OUT_DIR)/coral/examples/two_models_two_tpus_threaded \
	      $(BAZEL_OUT_DIR)/coral/examples/model_pipelining \
	      $(BAZEL_OUT_DIR)/coral/examples/classify_image \
	      $(BAZEL_OUT_DIR)/coral/examples/detect_image \
	      $(BAZEL_OUT_DIR)/coral/examples/backprop_last_layer \
	      $(BAZEL_OUT_DIR)/coral/examples/bug \
	      $(EXAMPLES_OUT_DIR)
