class CreateStockroomItem < ActiveRecord::Migration
  def change
    create_table "stockroom_items", force: :cascade do |t|
      t.string "name"
      t.integer  "item_count"
      t.datetime "created_at", null: false
      t.datetime "updated_at", null: false
    end
  end
end
