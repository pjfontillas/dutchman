require 'bunny'

namespace :mq do

  desc "Create queues"
  task :init do
    conn = Bunny.new
    conn.start
    ch = conn.create_channel
    ch.queue("orders")
    ch.queue("buffet")
  end
end
