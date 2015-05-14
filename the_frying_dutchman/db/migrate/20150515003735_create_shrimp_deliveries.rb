class CreateShrimpDeliveries < ActiveRecord::Migration
  def change
    create_table :shrimp_deliveries do |t|
      t.integer :num_shrimp
      t.timestamps null: false
    end
  end
end
