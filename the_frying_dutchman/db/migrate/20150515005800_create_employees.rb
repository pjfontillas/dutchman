class CreateEmployee < ActiveRecord::Migration
  def change
    create_table "employees", force: :cascade do |t|
      t.string "name"
      t.string "role"
      t.string "status"
    end
  end
end