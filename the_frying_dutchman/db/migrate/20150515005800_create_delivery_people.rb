class CreateDeliveryPeople < ActiveRecord::Migration
  def change
    create_table :delivery_people do |t|
      t.string :name
      t.string :status
    end
  end
end
