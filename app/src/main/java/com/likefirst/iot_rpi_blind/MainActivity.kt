package com.likefirst.iot_rpi_blind

import android.content.Intent
import android.net.Uri
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import androidx.recyclerview.widget.GridLayoutManager
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.google.android.material.snackbar.Snackbar
import com.google.firebase.ktx.Firebase
import com.google.firebase.storage.FirebaseStorage
import com.google.firebase.storage.ktx.storage
import com.likefirst.iot_rpi_blind.databinding.ActivityMainBinding
import java.net.URI

private lateinit var binding : ActivityMainBinding

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        setContentView(binding.root)

        val pathString = "noman"
        val storage = Firebase.storage
        val storageReference = storage.reference
        val pathReference = storageReference.child(pathString)
        val listRef = storageReference.child(pathString)

        if(pathReference == null){
            Snackbar.make(binding.mainStorageRv, "저장소에 사진이 없습니다.", Snackbar.LENGTH_SHORT).show()
        } else {
            // 저장소에 사진이 존재할 때
            listRef.listAll().addOnSuccessListener {
                val storageRvAdapter = MainStorageRVAdapter(it.items, this)   // it.items : 해당 저장소의 모든 사진을 리스트로 반환
                val gridLayoutManager = GridLayoutManager(this, 2)
                val rvItemdeco = MainStorageItemDeco()
                storageRvAdapter.setClickListener(object : MainStorageRVAdapter.ItemClickListener{
                    override fun gotoGallery(position : Int) {
                        val intent = Intent(this@MainActivity, GalleryActivity::class.java)
                        intent.putExtra("position", position)
                        intent.putExtra("path", pathString)
                        startActivity(intent)
                    }
                })
                rvItemdeco.initSize(this)
                binding.mainStorageRv.apply {
                    adapter = storageRvAdapter      // 사진을 리스트로 어댑터에 전달
                    layoutManager = gridLayoutManager
                    overScrollMode = RecyclerView.OVER_SCROLL_NEVER
                    addItemDecoration(rvItemdeco)
                }
            }
        }
    }
}