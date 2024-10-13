# Example: Simple Proto File

One common use case for wanting to create a dynamic protocol buffer is when the source `.proto` file that you will create the dynamic protocol buffer from is available to you, but want to add a few fields to the source protobuf, regardless of what is in the source protobuf.

For example, if you are a data engineer with an ETL pipeline ingesting the protobuf message and you want to provide a `process_time` field to it to mark the time in which the message went through your system. Regardless of what the incoming message looks like, you will always want to be using exactly that message, but with the `process_time` field added to it.

Static protocol buffers do not allow for this simple change: while a `.proto` file can source other `.proto` files, and protobuf `Message`s can be used within other messages, without the dynamic adjustments that this library provides, there is _no way to create a message from another message, but adding a few fields to it_ except either dynamically as provided in this library or by maintaining another `.proto` file that copies the bulk of the source `.proto` file, adding the fields of interest. This does not allow the [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principal to be respected, and it allows for careless errors in copying the source `.proto` file information into the destination `.proto` file.


