require 'bunny'

class WelcomeController < ApplicationController
  def index
    conn = Bunny.new
    conn.start
    channel = conn.create_channel
    buffetq = channel.queue('buffet')
    orderq = channel.queue('orders')

    @shrimp_in_buffet = buffetq.message_count
    @shrimp_in_stockroom = StockroomItem.where(name: 'shrimp').sum(:item_count)
    @delivery_person_status = Employee.where(name: 'Pat').first.status
    @orders_in_queue = orderq.message_count
  end

  def restock_refill
    conn = Bunny.new
    conn.start
    channel = conn.create_channel
    exchange = channel.default_exchange
    if params[:order]
      num = params[:num_shrimp].to_i
      exchange.publish({num: num, name: 'shrimp'}.to_json, routing_key: 'orders')
      @last_queue_status = 'added to order queue.'
    elsif params[:refill]
      shrimp_in_stock_room = 0
      biscuit_in_stock_room = 0      
      ActiveRecord::Base.transaction do
        shrimp_in_stock_room = StockroomItem.where(name: 'shrimp').sum(:item_count)
        biscuit_in_stock_room = StockroomItem.where(name: 'biscuit').sum(:item_count)
        StockroomItem.delete_all
      end
      
      biscuit_in_stock_room.times do
        exchange.publish('biscuit', routing_key: 'buffet')
      end     
      shrimp_in_stock_room.times do
        exchange.publish('shrimp', routing_key: 'buffet')
      end
       
    end

    redirect_to(action: :index)
  end
end
