package com.likefirst.iot_rpi_blind

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.recyclerview.widget.RecyclerView
import com.google.firebase.ktx.Firebase
import com.google.firebase.storage.ktx.storage
import com.likefirst.iot_rpi_blind.databinding.ActivityGalleryBinding

private lateinit var binding : ActivityGalleryBinding

class GalleryActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityGalleryBinding.inflate(layoutInflater)
        setContentView(binding.root)

        var curpos = intent.getIntExtra("position", 0)
        val pathString = intent.getStringExtra("path")!!
        val storageReference = Firebase.storage.reference
        val pathReference = storageReference.child(pathString)

        pathReference.listAll().addOnSuccessListener{
            val imgAdapter = GalleryVpAdapter(it.items)
            binding.galleryVp.apply {
                adapter = imgAdapter
                setCurrentItem(curpos, false)
            }
        }
    }
}